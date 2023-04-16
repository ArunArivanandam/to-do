function toggleCompletion(itemId) {
    let item = document.getElementById(`item${itemId}`);
    let label = item.nextElementSibling;
    if (item.checked) {
        label.classList.add('completed');
    } else {
        label.classList.remove('completed');
    }
}