<template>
  <div class="app">
    <div v-for="post in posts" :key="post.id" class="post">
      <div class="post__author">{{post.author}}</div>
      <div class="created">{{post.created_date}}</div>
      <h2 class="post__title">{{post.title}}</h2>
      <p class="post__text">{{post.text}}</p>
    </div>
  </div>
</template>

<script>
import {HTTP} from '../api/common'
export default {
  name: 'HelloWorld',
  data () {
    return {
      posts: []
    }
  },
  mounted () {
    HTTP
      .get('posts')
      .then(response => (this.posts = response.data))
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
