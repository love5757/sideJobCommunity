export default {
  name: 'App',
  data () {
    return {
      items: []
    }
  },
  methods: {
    created () {
      this.$axios.get('https://jsonplaceholder.typicode.com/posts')
        .then((response) => {
          console.log(response.data + 'HELLLP')
          this.items = response.data
        })
    }
  }
}
