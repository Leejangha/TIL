import { useState } from "react";

export default function Player({ name, symbol }) {
  const [isEditing, setIsEditing] = useState(false);

  function handleEditClick() {
<<<<<<< HEAD
    setIsEditing((editing) => !editing);
=======
    setIsEditing(!isEditing);
>>>>>>> de80b2257d9ab557280fb1b945cb1c76155118cc
  }

  let playerName = <span className="player-name">{name}</span>;
  // let btnCaption = 'Edit';

  if (isEditing) {
    playerName = <input type="text" required value={name} />;
<<<<<<< HEAD
    // btnCaption = 'Save';
=======
    // btnCaption = 'save';
>>>>>>> de80b2257d9ab557280fb1b945cb1c76155118cc
  }

  return (
    <li>
      <span className="player">
        {playerName}
        <span className="player-symbol">{symbol}</span>
      </span>
<<<<<<< HEAD
      <button onClick={handleEditClick}>{isEditing ? 'Save' : 'Edit'}</button>
=======
      <button onClick={handleEditClick}>{isEditing ? "Save" : "Edit"}</button>
>>>>>>> de80b2257d9ab557280fb1b945cb1c76155118cc
    </li>
  );
}
