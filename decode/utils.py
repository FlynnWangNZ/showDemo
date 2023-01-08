# auth: Flynn Wang
# date: 3/01/23
# desc:
import binascii
import json
import os
import struct

from showDemo.settings import BASE_DIR


class DecodeBase:
    head_format = {}
    tail_format = {}
    config_file = ''

    def __init__(self, hex_code: str):
        self.hex_code = hex_code
        self.head_length = 0
        self.tail_length = 0
        self.msg_type = ''

    def _is_endian(self):
        """TODO use try except to determine whether the hex code is big endian or not"""
        if self.hex_code:
            return True
        else:
            return False

    def _set_endian_format(self, content_type):
        """set the format of hex content"""
        if self._is_endian():
            return f'>{content_type}'
        else:
            return f'<{content_type}'

    def _get_json_content(self, content_format, hex_content):
        ret = {}
        byte_point = 0
        for item_name, item_type in content_format.items():
            content_length = struct.calcsize(item_type) * 2
            content_hex = hex_content[byte_point: byte_point + content_length]
            content_bin = binascii.unhexlify(content_hex)
            item_format = self._set_endian_format(item_type)
            content = struct.unpack(item_format, content_bin)[0]
            if type(content) == bytes:
                content = content.decode()
            ret[item_name] = content
            byte_point += content_length
        return ret

    @staticmethod
    def _get_hex_length(content_format):
        hex_format = ''
        for item_name, item_type in content_format.items():
            hex_format += item_type
        content_length = struct.calcsize(hex_format) * 2
        return content_length

    def get_head(self) -> dict:
        self.head_length = self._get_hex_length(self.head_format)
        head_hex = self.hex_code[:self.head_length]
        ret = self._get_json_content(self.head_format, head_hex)
        # specify the message type
        self.msg_type = head_hex[:2]
        return ret

    def get_body_format(self) -> dict:
        json_file = os.path.join(BASE_DIR, 'decode', 'format', self.config_file)
        with open(json_file, 'r') as f:
            format_all = json.load(f)
        body_format = format_all.get(self.msg_type)
        return body_format

    def get_body(self) -> dict:
        body_hex = self.hex_code[self.head_length:len(self.hex_code) - self.tail_length]
        ret = self._get_json_content(self.get_body_format(), body_hex)
        return ret

    def get_tail(self) -> dict:
        self.tail_length = self._get_hex_length(self.tail_format)
        tail_hex = self.hex_code[len(self.hex_code) - self.tail_length:]
        ret = self._get_json_content(self.tail_format, tail_hex)
        return ret

    def read(self):
        head_json = self.get_head()
        tail_json = self.get_tail()
        body_json = self.get_body()
        return {
            'head': head_json,
            'body': body_json,
            'tail': tail_json
        }


class DecodeFair(DecodeBase):
    pass


class DecodeFtd(DecodeBase):
    head_format = {
        'msgType': 'b',
        'extendLength': 'b',
        'msgLength': 'h'
    }

    tail_format = {
        'checkSum': 'h'
    }

    config_file = 'dtf.json'


class DecodeFtdc(DecodeBase):
    pass


class DecodeFactory:
    """expose this class as user interface"""

    def __init__(self, project, hex_code):
        self.project = project
        self.hex_code = hex_code

    def get_product(self):
        if self.project == 'DTO':
            return DecodeFair(self.hex_code)
        elif self.project == 'DTF':
            return DecodeFtd(self.hex_code)
        elif self.project == 'DTS':
            return DecodeFtdc(self.hex_code)
        else:
            return None
