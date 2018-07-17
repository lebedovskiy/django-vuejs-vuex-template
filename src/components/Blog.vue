<template lang="pug">
  .postlist
    div(class='post' v-for='post in posts' :key='post.id')
      h2.post__title {{post.title}}
      .post__created {{post.created_date | date_time}}
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
  },
  filters: {
    capitalize: (value) => {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    },
    date_time: (value) => {
      return value.substr(12, 4) + ' ' + value.substr(8, 2) + '.' + value.substr(5, 2) + '.' + value.substr(0, 4)
    }
  }
}
</script>

<style lang="stylus">
  .postlist
    font-family Bahnschrift
    width 60%
    margin 0 auto
    @media screen and (max-width: 996px)
      width 100%

  .post
    margin 2%
    width 95%

  .post__author
    margin 0.5em 0

  .post__created
    font-size 0.8em

</style>
