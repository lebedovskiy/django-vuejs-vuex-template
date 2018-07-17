<template lang="pug">
  .postlist
    div(class='post' v-for='post in posts' :key='post.id')
      .post__author {{post.owner}}
      .post__created {{post.created_date}}
      h2.post__title {{post.title}}
      p.post__text {{post.text}}
</template>

<script>
import {HTTP} from '../api/common'

export default {
  name: 'Blog',
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

<style lang="stylus">
  .postlist
    float left
    margin 10px
    margin-top 50px
    padding 5px 0
    width 90%

  .post__title
    font-weight: bold

  .post__text
    line-height: 1.5

  .post__author
    margin: 10px 0

</style>
