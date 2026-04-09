export default function updateStudentGradeByCity(listStudents, city, newGrades) {
    
    return listStudents.filter((student) => student.location === city).map((student) => {
        const studentGrade = newGrades.filter((grade) => grade.studentId === student.id);
        const finalGread = studentGrade.length > 0 ? studentGrade[0].grade : 'N/A';

        return {
            ...student,
            grade: finalGread
        };
    });
}