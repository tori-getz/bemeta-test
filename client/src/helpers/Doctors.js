export function findDoctor (doctors, id) {
    console.log(doctors, id)
    for (let doctor of doctors) {
        if (doctor.id === id) {
            return {
                name: doctor.fields["Имя"],
                methods: doctor.fields["Методы"],
                photo: doctor.fields["Фотография"][0].url
            }
        }
    }
}

export function getDoctorList () {
    
}