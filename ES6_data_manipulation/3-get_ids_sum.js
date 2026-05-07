export default function getStudentIdsSum(students) {
    return students.reduce((acc, id) => acc + id.id, 0)
}