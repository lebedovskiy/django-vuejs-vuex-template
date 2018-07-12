<template>
  <div id="app">
    <div v-for="post in posts" :key="post.id">
      <div class="post__author">{{post.author}}</div>
      <div class="created">{{post.created_date}}</div>
      <div class="post__title">{{post.title}}</div>
      <div class="post__text">{{post.text}}</div>
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
