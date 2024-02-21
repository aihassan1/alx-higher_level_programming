#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

// Function to count the number of completed tasks for a given user ID
function trueCounter(data, userId) {
  let counter = 0;
  // Loop through each item in the data
  for (const item of data) {
    // Check if the item belongs to the specified user ID and if it's completed
    if (item.userId === userId && item.completed === true) {
      counter++;
    }
  }
  // Return an object with the user ID as the key and the count as the value
  return { [userId]: counter };
}

// Make a request to the provided URL
request(url, (error, response, body) => {
  // Handle errors
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body into JSON format
  const bodyData = JSON.parse(body);
  // Initialize an empty object to store the results
  const usersCompletedTasks = {};

  // Iterate through each item in the response body data
  for (const item of bodyData) {
    // Call the trueCounter function to count completed tasks for the current user ID
    const result = trueCounter(bodyData, item.userId);

    // Assign the result to the usersCompletedTasks object
    Object.assign(usersCompletedTasks, result);
  }

  // Output the object containing the count of completed tasks for each user ID
  console.log(usersCompletedTasks);
});
