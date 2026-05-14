const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, content) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = content
        .split('\n')
        .filter((line) => line.length > 0)
        .slice(1);
      console.log(`Number of students: ${lines.length}`);
      const groups = {};
      lines.forEach((line) => {
        const fields = line.split(',');
        const firstname = fields[0];
        const field = fields[3];
        if (!groups[field]) groups[field] = [];
        groups[field].push(firstname);
      });
      Object.keys(groups).forEach((field) => {
        console.log(
          `Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`,
        );
      });
      resolve();
    });
  });
}

module.exports = countStudents;
