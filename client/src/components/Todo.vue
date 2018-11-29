<template>
  <div class="container">
    <h3>Todo</h3>
    <hr>
    <button type="button" class="btn btn-success btn-sm" v-b-modal.todo-modal>Add Todo</button>
            <br><br>
    <div class="list-group">
      <div class="list-group-item todos-header">
        <div class="row">
          <div class="col-md-1 col-sm-1"> Id </div>
          <div class="col-md-3 col-sm-6"> Content </div>
          <div class="col-md-2 col-sm-4"> Created </div>
          <div class="col-md-1 col-sm-1"> Done? </div>
        </div>
      </div>
         <div class="list-group-item" v-for="(todo, index) in todos" :key="index">
             <div class="row">
          <div class="col-md-1 col-sm-1"> {{index+1}} </div>
          <div class="col-md-3 col-sm-6"> {{todo.content}} </div>
          <div class="col-md-2 col-sm-4"> {{todo.created}} </div>
          <div class="col-md-1 col-sm-1">  <span v-if="todo.done">Yes</span>
                <span v-else>No</span></div>
          <div class="col-md-1 ml-auto col-sm-4 text-center"><button type="button"
          class="btn btn-danger btn-sm" @click="onDeleteTodo(todo)"> Delete</button></div>
           <div class="col-md-1 col-sm-4 text-center"><button type="button"
           class="btn btn-warning btn-sm"
           @click="onToggleTodo(todo)">
                  Toggle</button> </div>
            <div class="col-md-1 col-sm-4 text-center"><button type="button"
            class="btn btn-warning btn-sm" v-b-modal.edit-todo-modal @click="onEditTodo(todo)">
                  Edit</button> </div>
         </div>
          </div>
    </div>
    <b-modal ref="addTodoModal" id="todo-modal" title="Add a new todo" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group" label="Content:" label-for="form-content-input">
          <b-form-input id="form-content-input" type="text" v-model="addTodoForm.content"
          required placeholder="Enter Content">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editTodoModal" id="edit-todo-modal" title="Edit a todo" hide-footer>
      <b-form @submit="onSubmitUpdateTodo" @reset="onCancelUpdate" class="w-100">
        <b-form-group id="form-content-edit-group" label="Content:" label-for="form-content-input">
          <b-form-input id="form-content-edit-input" type="text" v-model="editForm.content"
          required placeholder="Enter Content">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Todo',
  data() {
    return {
      todos: [],
      addTodoForm: {
        content: '',
      },
      editForm: {
        id: '',
        content: '',
        done: false,
      },
      message: '',
      showMessage: false,

    };
  },
  methods: {
    getTodos() {
      const path = 'http://localhost:5000/todos/';
      axios.get(path)
        .then((res) => {
          this.todos = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTodo(payload) {
      const path = 'http://localhost:5000/todos/';
      axios.post(path, payload)
        .then(() => {
          this.getTodos();
          this.message = 'Todo added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTodos();
        });
    },
    onEditTodo(todo) {
      this.editForm.id = todo.id;
      this.editForm.content = todo.content;
      this.editForm.done = todo.done;
    },

    initForm() {
      this.addTodoForm.content = '';
      this.editForm.id = '';
      this.editForm.content = '';
      this.editForm.done = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTodoModal.hide();


      const payload = {
        content: this.addTodoForm.content,
      };
      this.addTodo(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTodoModal.hide();
      this.initForm();
    },
    removeTodo(todoId) {
      const path = `http://localhost:5000/todos/${todoId}/`;
      axios.delete(path)
        .then(() => {
          this.getTodos();
          this.message = 'Todo delete!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTodos();
        });
    },
    onDeleteTodo(todo) {
      this.removeTodo(todo.id);
    },
    onUpdateTodo(todoId, todoContent, todoDone) {
      const path = `http://localhost:5000/todos/${todoId}/`;
      const payload = {
        content: todoContent,
        done: todoDone,
      };
      axios.put(path, payload)
        .then(() => {
          this.getTodos();
          this.message = 'Todo added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTodos();
        });
    },
    onSubmitUpdateTodo(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();


      this.onUpdateTodo(this.editForm.id, this.editForm.content, this.editForm.done);
      this.initForm();
    },
    onToggleTodo(todo) {
      this.onUpdateTodo(todo.id, todo.content, !todo.done);
    },
    onCancelUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getTodos();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.todos-header{
    background-color: #111111;
    color:white;
}
</style>
