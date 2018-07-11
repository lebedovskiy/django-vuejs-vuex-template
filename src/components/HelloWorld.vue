<template>
  <div id="app">
    <div class="post">{{posts.author}}</div>
      <div class="post__title">{{posts.title}}</div>
      <div class="post__text">{{posts.text}}</div>

  </div>
</template>

<script>
// TODO: разобратьс с объектом/массивом posts! Почему он массив объектов?
// Что правильнее - научить джанго отдавать посты по одному или разгребать массив объектов через vue
import {HTTP} from '../api/common'
export default {
  name: 'HelloWorld',
  data () {
    return {
      posts: [],
      author: [],
      title: [],
      text: []
    }
  },
  mounted () {
    HTTP
      .get('posts')
      .then(response => (this.posts = response.data[0]))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
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
</style>
