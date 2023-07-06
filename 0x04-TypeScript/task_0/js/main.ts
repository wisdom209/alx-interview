interface Student {
  firstName: string;
  lastName: string;
  location: string;
}

const student1: Student = {
  firstName: 'Guillaume',
  lastName: 'Salva',
  location: 'San Francisco',
};

const student2: Student = {
  firstName: 'Jullien',
  lastName: 'Barbier',
  location: 'California',
};

let studentArray: any = [student1, student2];

const tbody: any = document.querySelector('tbody');

studentArray.forEach((v: any) => {
  tbody.append(`
	<tr>
	${v.firstName}
	</tr>
	<tr>
	${v.lastName}
	</tr>
	<tr>
	${v.location}
	</tr>
	`);
});
