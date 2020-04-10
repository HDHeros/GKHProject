<template>
	<!-- <div>
        <ul>
        <li v-for="users in info.data" v-bind:key="users.id">
          {{users.mobile_phone.numder_mobile_phone}}
        </li>  
      </ul>
	</div>-->
	<v-card>
		<v-card-title>
			Сотрудники
			<v-spacer></v-spacer>
			<v-text-field v-model="search" append-icon="mdi-magnify" label="Поиск" single-line hide-details></v-text-field>
		</v-card-title>
		<v-data-table :headers="headers" :items="info.data" :search="search"></v-data-table>
	</v-card>
</template>

<script>
import axios from "axios";
export default {
	mounted() {
		axios.get("http://127.0.0.1:8000/api/v1/user/").then(response => {
			this.info = response.data.data;
		});
	},
	data() {
		return {
			search: "",
			info: [],
			headers: [
				{
					text: "Фамилия",
					value: "surname"
				},
		{ text: "Имя", value: "name" },
        { text: "Отчество", value: "middle_name" },
        { text: "Мобильный телефон", value: "mobile_phone.numder_mobile_phone"},
        { text: "Городской телефон", value: "work_phone.number_work_phone"},
        { text: "Должность", value: "post.name_post"},
        { text: "Кабинет", value: "kab.number_kab"},
        { text: "Отдел", value: "kab.branch.name_branch"}
			],
		};
	}
};
</script>

<style lang="scss" scoped></style>