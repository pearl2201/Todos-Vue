import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import Todo from '@/components/Todo';

Vue.use(Router);

export default new Router({
  routes: [{
    path: '/',
    name: 'Todo',
    component: Todo,
  }, {
    path: '/hello',
    name: 'HelloWorld',
    component: HelloWorld,
  }],
  mode: 'history',
});
