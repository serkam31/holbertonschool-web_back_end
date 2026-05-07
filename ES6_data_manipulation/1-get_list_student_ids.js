export default function getListStudentIds(element) {
    if (Array.isArray(element)) {
        return element.map((select) => select.id)
    } else return [];
}