import { useState } from "react";
import { formatString } from "./helpers";

export const HierarchyDropdowns = ({
  data,
  onChange,
  selected,
  level = 1,
  isEnumeration = false,
}) => {
  const [enumeration, setEnumeration] = useState()

  const handleChange = (level, value, isEnumeration) => {
    onChange(level, value, isEnumeration);
    if(isEnumeration) {
      setEnumeration(value)
    }
  };

  const Dropdown = ({ data, level, isEnumeration }) => {
    if (data instanceof Array) {
      return (
        <select
          className={
            isEnumeration ? "select select-accent" : "select select-primary"
          }
          onChange={(e) => handleChange(level, e.target.value, isEnumeration)}
          value={enumeration}
        >
          {data.map((value, index) => (
            <option value={value} key={index}>
              {formatString(value)}
            </option>
          ))}
        </select>
      );
    } else if (data instanceof Object) {
      return (
        <select
          className="select select-primary"
          onChange={(e) => handleChange(level, e.target.value, isEnumeration)}
          value={selected[level]}
        >
          <option value={0}>Select Level {level}</option>
          {Object.entries(data).map((value, index) => (
            <option value={value[0]} key={index + 1}>
              {formatString(value[0])}
            </option>
          ))}
        </select>
      );
    }
  };

  return (
    <div className="flex space-x-4 ">
      <Dropdown data={data} level={level} isEnumeration={isEnumeration} />

      {selected[level] && data[selected[level]]?.enumerations && (
        <HierarchyDropdowns
          data={data[selected[level]]?.enumerations}
          onChange={onChange}
          selected={selected}
          level={level + 1}
          isEnumeration={true}
        />
      )}

      {selected[level] && data[selected[level]]?.children && (
        <HierarchyDropdowns
          data={data[selected[level]]?.children}
          onChange={onChange}
          selected={selected}
          level={level + 1}
        />
      )}
    </div>
  );
};
