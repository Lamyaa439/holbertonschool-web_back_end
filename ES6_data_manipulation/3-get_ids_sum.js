export default function getStudentIdsSum(listStudents) {
    return listStudents.reduce(
        (accumulator, student) => {
        return accumulator + student.id;
    }, 0);
}