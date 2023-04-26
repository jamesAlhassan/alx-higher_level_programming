#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, res, content) => {
  if (err) {
    console.log(err);
    return;
  }

  const tasksCompleted = {};
  content.map((task) => {
    if (task.completed) {
      if (!tasksCompleted[task.userId]) {
        tasksCompleted[task.userId] = 1;
      } else {
        tasksCompleted[task.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
