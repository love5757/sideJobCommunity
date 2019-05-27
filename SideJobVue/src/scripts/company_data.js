
export default {
  name: 'chickenMain',
  data () {
    return {
      items: [],
      img_src: 'http://www.urbanbrush.net/web/wp-content/uploads/edd/2018/02/web-20180211134119206041.png'
    }
  },
  created () {
    this.$axios.get('localhost:3000/getRecruitList')
      .then((response) => {
        console.log(response.data + 'HELLLP')
        this.items = response.data
      })
  }
}
