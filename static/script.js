document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("todo-form");
  const todoList = document.getElementById("todo-list");

  async function fetchTodos() {
    const response = await fetch("/todos/");
    const todos = await response.json();
    todoList.innerHTML = "";
    todos.forEach(todo => {
      const li = document.createElement("li");
      li.textContent = `${todo.title}: ${todo.description}`;
      const delBtn = document.createElement("button");
      delBtn.textContent = "Delete";
      delBtn.onclick = async () => {
        await fetch(`/todos/${todo.id}`, { method: "DELETE" });
        fetchTodos();
      };
      li.appendChild(delBtn);
      todoList.appendChild(li);
    });
  }

  form.onsubmit = async e => {
    e.preventDefault();
    const id = document.getElementById("id").value;
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    await fetch("/todos/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: Number(id), title, description, completed: false })
    });
    form.reset();
    fetchTodos();
  };

  fetchTodos();
});
