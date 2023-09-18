export const HierarchyDropdowns = ({ data, onChange, selected, level = 1 }) => {
  const handleChange = (level, value) => {
    console.log(selected);
    onChange(level, value);
  };

  const Dropdown = ({ data, level }) => {
    if (data instanceof Array) {
      return (
        <select className="select select-primary">
          {data.map((value, index) => (
            <option value={value} key={index}>
              {value}
            </option>
          ))}
        </select>
      );
    } else if (data instanceof Object) {
      return (
        <select
          className="select select-primary"
          onChange={(e) => handleChange(level, e.target.value)}
          value={selected[level]}
        >
          <option value={0}>Select Level {level}</option>
          {Object.entries(data).map((value, index) => (
            <option value={value[0]} key={index + 1}>
              {value[0]}
            </option>
          ))}
        </select>
      );
    }
  };

  return (
    <div className="flex space-x-4 ">
      <Dropdown data={data} level={level} />

      {selected[level] && data[selected[level]]?.enumerations && (
        <HierarchyDropdowns
          data={data[selected[level]]?.enumerations}
          onChange={onChange}
          selected={selected}
          level={level + 1}
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
