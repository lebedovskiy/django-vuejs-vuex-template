<template lang="pug">
.resume
    .presentation
      h2.presentation__text {{presentation.title}}
      img.presentation__img(width='100%', src='../assets/1530346884.jpg')
</template>

<script>
import {HTTP} from '../api/common'
export default {
  name: 'Resume',
  data () {
    return {
      presentation: []
    }
  },
  mounted () {
    HTTP
      .get('posts')
      .then(response => (this.presentation = response.data[0]))
  }
}
</script>

<style lang="stylus">
  .resume
    font-family Bahnschrift
    width 60%
    margin 0 auto
    @media screen and (max-width: 996px)
      width 100%

  .presentation
    margin 1em
    overflow auto

  .presentation__text
    @media screen and (orientation: landscape)
      float left
      margin 1%
      width 49%

  .presentation__img
    @media screen and (orientation: landscape)
      float right
      width 49%

  .main__text
    margin 2%
    padding 0 1%
    width 95%
</style>
