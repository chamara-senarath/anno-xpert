import { useState } from "react";

export default function SearchSection({ onSearch }) {
  const [query, setQuery] = useState("");
  const [matchLevel, setMatchLevel] = useState(8);
  const [isCaseSensitive, setIsCaseSensitive] = useState(false);

  const handleOnClickSearch = () => {
    onSearch(query, matchLevel, isCaseSensitive);
  };

  return (
    <div className="flex items-center border p-2 rounded-lg">
      <input
        type="text"
        placeholder="Type here"
        className="input input-bordered input-primary w-full max-w-xs"
        onChange={(e) => setQuery(e.target.value)}
      />
      <div className="flex items-center space-x-12 w-full ml-4">
        <div className="flex">
          <label className="cursor-pointer label">
            <span className="label-text">Case Sensitive</span>
            <input
              type="checkbox"
              className="toggle toggle-primary ml-4"
              checked={isCaseSensitive}
              onChange={(e) => setIsCaseSensitive(e.target.checked)}
            />
          </label>
        </div>
        <div className="flex flex-col items-center">
          <span>Match Level: {matchLevel}</span>
          <input
            className="range range-primary range-xs"
            value={matchLevel}
            type="range"
            min={1}
            max="10"
            step={1}
            onChange={(e) => {
              setMatchLevel(e.target.value);
            }}
          />
        </div>
      </div>
      <button className="btn btn-primary" onClick={handleOnClickSearch}>
        Search
      </button>
    </div>
  );
}
