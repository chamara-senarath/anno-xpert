export default function ResultView({ results }) {
  return (
    <div className="flex flex-col w-full">
      <span>{results.length} results found</span>
      <div className="min-h-screen flex border rounded-lg">
        <div className="flex flex-col space-y-4 px-4 py-2 max-h-[calc(100vh-4rem)] overflow-y-auto">
          {results.map((item, index) => (
            <div className="outline outline-accent p-4 rounded-lg" key={index}>
              <label className="text-lg font-semibold">{item.local_name}</label>
              <div className="border border-gray-300 p-2 rounded-md">
                {item.text}
              </div>
              <div className="flex space-x-2 mt-2">
                {item?.attributes.map((attribute, index) => (
                  <div className="badge badge-primary" key={index}>
                    {attribute[0]} : {attribute[1]}
                  </div>
                ))}
              </div>
              <div className="bg-gray-200 mt-2 px-2 rounded-md">
                {item.ancestors}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
