// src/components/KanbanColumn.js

import React from 'react';


function KanbanColumn({ title, tasks }) {
  return (
    <div className="kanban-column">
      <h2>{title}</h2>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>{task}</li>
        ))}
      </ul>
    </div>
  );
}

export default KanbanColumn;
