<template lang="pug">
  #app
   div(class='post' v-for="post in posts" :key="post.id")
      .post__author {{post.author}}
      .created {{post.created_date}}
      h2.post__title {{post.title}}
      p.post__text {{post.text}}
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
p{
  line-height: 1.5;
}
</style>
