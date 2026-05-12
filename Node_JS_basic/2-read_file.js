const fs = require("fs");

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, "utf8");
    const lines = content
      .split("\n")
      .filter((line) => line.length > 0)
      .slice(1);
    console.log(`Number of students: ${lines.length}`);
    const groups = {};
    lines.forEach((line) => {
      const fields = line.split(",");
      const firstname = fields[0];
      const field = fields[3];
      if (!groups[field]) groups[field] = [];
      groups[field].push(firstname);
    });
    Object.keys(groups).forEach((field) => {
      console.log(
        `Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(", ")}`,
      );
    });
  } catch (e) {
    throw new Error("Cannot load the database");
  }
}
module.exports = countStudents;
