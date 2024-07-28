document.addEventListener("DOMContentLoaded", () => {
    const addItem = document.getElementById('add_item');
    const removeItem = document.getElementById('remove_item');
    const clearList = document.getElementById('clear_list');
    const list = document.querySelector('.my_list');
  
    addItem.addEventListener('click', () => {
      const newItem = document.createElement('li');
      newItem.textContent = 'Item';
      list.appendChild(newItem);
    });
  
    removeItem.addEventListener('click', () => {
      if (list.children.length > 0) {
        list.removeChild(list.lastElementChild);
      }
    });
  
    clearList.addEventListener('click', () => {
      while (list.firstChild) {
        list.removeChild(list.firstChild);
      }
    });
  });
  