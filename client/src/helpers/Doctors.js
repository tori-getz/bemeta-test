export function findDoctor (doctors, id) {
    for (let doctor of doctors) {
        if (doctor.id === id) {
            return {
                name: doctor.fields["Имя"],                     //
                methods: doctor.fields["Методы"],               //  Чувство, будто это можно реализовать лучше
                photo: doctor.fields["Фотография"][0].url       //
            }
        }
    }
}

export function getDoctorsList (doctors) {
    let links = [];
    for (let doctor of doctors) {
        links.push({
            id: doctor.id,
            name: doctor.fields["Имя"],
            path: `/doctor/${doctor.id}`
        });
    }
    console.log(links);
    return links;
}