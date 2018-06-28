// {
//   "organization": ["ABC Corp"],
//   "sourceControl": ["github"],
//   "collaborationTools": ["slack","jira"],
//   "appContainers": ["springboot", "vue", "mongo"],
//   "testLibraries": ["junit", "jest"]
// }


Vue.component('foundation-tag', {
	props: ['struct'],
	template: '<div class="foundations">{{ struct }}</div>'
})

var foundations = new Vue({
	el: '#foundations-app',
	data: {
		list: []
	},
	mounted(){
		var vueScope = this;
		axios.get('example1.json')
		.then(function (response) {
			vueScope.list = response.data.hosting;
		})
		.catch(function (error) {
			console.log(error);
		});
	}
})


Vue.component('environment-tag', {
	props: ['struct'],
	template: '<div class="floors">{{ struct }}</div>'
})

var environment = new Vue({
	el: '#environment-app',
	data: {
		list: []
	},
	mounted(){
		var vueScope = this;
		axios.get('example1.json')
		.then(function (response) {
			vueScope.list = response.data.environments;
		})
		.catch(function (error) {
			console.log(error);
		});
	}
})
