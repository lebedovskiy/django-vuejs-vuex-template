<template lang="pug">
  .app
   div(class='post' v-for='post in posts' :key='post.id')
      .post__author {{author}}
      .post__created {{post.created_date}}
      h2.post__title {{post.title}}
      p.post__text {{post.text}}
</template>

<script>
import {HTTP} from '../api/common'
export default {
  name: 'HelloWorld',
  data () {
    return {
      author: 'lebedovskiy',
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
<style  lang="stylus">
.post__title
  font-weight: normal

.post__text
  line-height: 1.5

.post__author
  margin: 1em
</style>
