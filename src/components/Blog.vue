<template lang="pug">
  .postlist
    div(class='post' v-for='post in posts' :key='post.id')
      .post__author {{author}}
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
      author: 'Lebedovskiy',
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

<style  lang="stylus">
.postlist
  margin 20px 10px
  width 60%
  float left

.post__title
  font-weight: normal

.post__text
  line-height: 1.5

.post__author
  margin: 10px 0

</style>
