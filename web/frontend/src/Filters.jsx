import { useState, useEffect } from "react";

useEffect;
export default function Filters({ results, onSelect, selected, clear }) {
  const [filters, setFilters] = useState([]);

  useEffect(() => {
    if (results && results.length) {
      const localNames = [];
      results.forEach((result) => {
        if (!localNames.includes(result.local_name)) {
          localNames.push(result.local_name);
        }
      });
      setFilters(localNames);
    }
  }, [results]);

  return (
    <div className="flex w-1/4 flex-col h-full ">
      <div>Filters</div>
      <div className="grid grid-cols-2  gap-2  border rounded-lg py-10 px-2">
        {filters.map((filter, index) => (
          <button
            className={
              selected.includes(filter)
                ? "btn btn-success"
                : "btn btn-outline btn-success"
            }
            key={index}
            onClick={() => {
              onSelect(filter);
            }}
          >
            {filter}
          </button>
        ))}
      </div>
      <button className="btn btn-outline btn-primary mt-4" onClick={clear}>Clear Filters</button>
    </div>
  );
}
