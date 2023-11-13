// src/components/HomePage.js
import React from 'react';

import KanbanColumn from './KanbanColumn';

const tasks = {
  todo: ['Task 1', 'Task 2'],
  inProgress: ['Task 3'],
  done: ['Task 4', 'Task 5'],
};

function HomePage() {
  return (
    <div className="kanban-board">
      <KanbanColumn title="To Do" tasks={tasks.todo} />
      <KanbanColumn title="In Progress" tasks={tasks.inProgress} />
      <KanbanColumn title="Done" tasks={tasks.done} />
    </div>
  );
}

export default HomePage;
