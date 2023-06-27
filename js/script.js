// // Get the checkboxes
// const checkboxes = document.querySelectorAll('input[name="age-range"]');

// // Add event listener to each checkbox
// checkboxes.forEach(checkbox => {
//     checkbox.addEventListener('change', function () {
//         const selectedValues = Array.from(checkboxes)
//             .filter(checkbox => checkbox.checked)
//             .map(checkbox => checkbox.value);

//         // Filter the items based on selected values
//         const items = document.querySelectorAll('.item');
//         items.forEach(item => {
//             const itemClasses = Array.from(item.classList);
//             if (selectedValues.length === 0 || selectedValues.some(value => itemClasses.includes(value))) {
//                 item.style.display = 'block';
//             } else {
//                 item.style.display = 'none';
//             }
//         });
//     });
// });