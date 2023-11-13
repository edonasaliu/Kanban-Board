// src/components/NewTaskPage.js
import React from 'react';

function NewTaskPage() {
  return (
    <div className="new-task-page">
      <form>
        <label>
          Task Title:
          <input type="text" name="title" />
        </label>
        <button type="submit">Add Task</button>
      </form>
    </div>
  );
}

export default NewTaskPage;
