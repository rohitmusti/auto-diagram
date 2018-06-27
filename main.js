Vue.component('infrastructure', {
	props: ['struct'],
	template: '<div class="foundations">{{ struct.text }}</div>'
})

var app1 = new Vue({
	el: '#app-1',
	data: {
		list: []
	},
	mounted(){
		var temp = this;
		axios.get('example.json')
		.then(function (response) {
			temp.list = response.data;
		})
		.catch(function (error) {
			console.log(error);
		});
	}
})

var app2 = new Vue({
	el: '#app-2',
	data: {
		message: 'You loaded this page on' + new Date().toLocaleString()
	}
})
