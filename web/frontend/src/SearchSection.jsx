import { useState } from "react";

export default function SearchSection({ onSearch }) {
  const [query, setQuery] = useState("");

  const handleOnClickSearch = () => {
    onSearch(query);
  };

  return (
    <div className="flex">
      <input
        type="text"
        placeholder="Type here"
        className="input input-bordered input-primary w-full max-w-xs"
        onChange={(e) => setQuery(e.target.value)}
      />
      <button className="btn btn-primary" onClick={handleOnClickSearch}>
        Search
      </button>
    </div>
  );
}
