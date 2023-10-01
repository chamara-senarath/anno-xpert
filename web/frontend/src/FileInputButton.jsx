import { useState, useRef } from "react";

function FileInputButton({handler, buttonName}) {
  const fileInputRef = useRef(null);

  const handleFileInputChange = (e) => {
    const file = e.target.files[0];
    handler(file);
  };

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  return (
    <div className="relative inline-flex rounded-md shadow-sm">
      <button
        type="button"
        onClick={handleButtonClick}
        className="btn btn-sm btn-primary"
      >
        {buttonName}
      </button>
      <input
        ref={fileInputRef}
        type="file"
        className="hidden"
        onChange={handleFileInputChange}
      />
    </div>
  );
}

export default FileInputButton;
