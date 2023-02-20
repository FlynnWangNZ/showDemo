$("#course").on("change", function (event) {
    // get value of course
    const course_id = $(this).val();
    $.ajax({
        url: "",
        data: {"course_id": course_id},
        type: "POST",
        dataType: "json",
        async: false,
        success: function (data) {
            const $tbody = $(".table>tbody");
            $tbody.empty();
            var content = '';
            for (var i = 0; i < data.length; i++) {
                const row = data[i];
                content += '<tr>';
                content += '<td>' + row.name + '</td>';
                content += '<td>' + row.marks + '</td>';
                content += '<td>' + row.percentage + '</td>';
                content += '<td><input type="number" step="0.1" class="form-control score" placeholder="YourScore"/></td>'
                content += '</tr>';
            }
            $tbody.append(content);
        },
        error: function (data) {
            console.error(data);
        }
    })
})

class GradeScale{
    constructor(grade, color) {
        this.grade = grade;
        this.color = color;
    }
}

function getGrade(score) {
    if (score >= 90 && score <= 100) {
        return new GradeScale('A+', '#10F20A')
    } else if (score >= 85) {
        return new GradeScale('A', '#66F12A')
    } else if (score >= 80) {
        return new GradeScale('A-', '#66F12A')
    } else if (score >= 75) {
        return new GradeScale('B+', '#66F12A')
    } else if (score >= 70) {
        return new GradeScale('B', '#D5F134')
    } else if (score >= 65) {
        return new GradeScale('B-', '#F1E734')
    } else if (score >= 60) {
        return new GradeScale('C+', '#F2B216')
    } else if (score >= 55) {
        return new GradeScale('C', '#F29E2E')
    } else if (score >= 50) {
        return new GradeScale('C-', '#EC761C')
    } else {
        return new GradeScale('D', '#F4370E')
    }
}

$('.score').on("change", function () {
    // get sum score
    var sum_score = 0;
    $('.table>tbody').find('tr').each(function () {
        var total_marks = parseFloat($(this).find('td:eq(1)').text());
        var mark = $(this).find('td:eq(3)>input').val();
        if (mark === '') {
            mark = 0
        } else {
            mark = parseFloat(mark);
        }
        var percentage = parseFloat($(this).find('td:eq(2)').text());
        var score = mark / total_marks * percentage;
        sum_score += score;
    })
    sum_score = sum_score.toFixed(2);

    // show sum score
    $('#sum_score').text(sum_score);

    // get grade
    var gradeScale = getGrade(sum_score);
    // show grade
    $('#grade').text(gradeScale.grade);
    // calculate color
    $('#grade').css('background-color', gradeScale.color);
})