<template>
  <div>
    <h1>To-Do List</h1>
    <input v-model="newTask" @keyup.enter="addTask" placeholder="Add a new task" />
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" v-model="todo.completed" /> {{ todo.task }}
        <button @click="removeTask(todo.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todos: [],
      newTask: '',
    };
  },
  methods: {
    async fetchTodos() {
      const response = await fetch('http://localhost:8000/todos');
      this.todos = await response.json();
    },
    async addTask() {
      const newTodo = { id: Date.now(), task: this.newTask, completed: false };
      await fetch('http://localhost:8000/todos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTodo),
      });
      this.newTask = '';
      this.fetchTodos();
    },
    async removeTask(id) {
      await fetch(`http://localhost:8000/todos/${id}`, { method: 'DELETE' });
      this.fetchTodos();
    },
  },
  mounted() {
    this.fetchTodos();
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
