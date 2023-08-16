const workshopBlocks = document.querySelectorAll('.workshop-item');
const subjectCheckboxes = document.querySelectorAll('input[name="subject-select"]');
const gradeRangeCheckboxes = document.querySelectorAll('input[name="grade-range"]');
const classTimeCheckboxes = document.querySelectorAll('input[name="class-time"]');


subjectCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', filterWorkshops);
});

gradeRangeCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', filterWorkshops);
});

classTimeCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', filterWorkshops);
});
// workshop filtering func
function filterWorkshops() {

    const selectedSubjects = Array.from(subjectCheckboxes)
        .filter((checkbox) => checkbox.checked)
        .map((checkbox) => checkbox.value);

    // Ex: ["grade-0"]
    const selectedGradeRanges = Array.from(gradeRangeCheckboxes)
        .filter((checkbox) => checkbox.checked)
        .map((checkbox) => checkbox.value);

    // Ex: ["grade-0"]
    const selectedClassTimes = Array.from(classTimeCheckboxes)
        .filter((checkbox) => checkbox.checked)
        .map((checkbox) => checkbox.value);

    // trying to make it so having nothing selected shows everything
    noSelection = (selectedGradeRanges.length == 0 && selectedSubjects.length == 0 && selectedClassTimes.length == 0)
    workshopBlocks.forEach((block) => {
        // for each block, decide if show or not
        const show = noSelection ||
            selectedSubjects.some((subject) => block.classList.contains(subject)) || // At least one selected subject matches
            selectedGradeRanges.some((gradeRange) => block.classList.contains(gradeRange)) ||// At least one selected grade range matches
            selectedClassTimes.some((classTime) => block.classList.contains(classTime));

        if (!show) {
            block.classList.add('collapse')
        } else {
            block.classList.remove('collapse');
        }
    });
}
