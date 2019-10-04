//
//
// #app > div > span:nth-child(2) > div > div > div > div > div > div > div > div
//
//
// //*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div
//
// function getContactStr(key){
// 	let elems = document.getElementsByClassName(key)
// 	output = ""
// 	let idx = 0
// 	while(idx < elems.length){
// 		output += "\n" + elems[idx].innerText.split("\n").join(",")
// 		idx++;
// 	}
// 	return output
// }
//
//
// function crawl(key, output){
// 	let temp = getContactStr(key)
// 	console.save(temp, output)
// }
//
//
// crawl("_1v8mQ", "2.csv")
//
//

(function (console) {
  console.save = function (data, filename) {
    if (!data) {
      console.error('Console.save: No data');
      return;
    }

    if (!filename) filename = 'console.json';

    if (typeof data === 'object') {
      data = JSON.stringify(data, undefined, 4);
    }

    const blob = new Blob([data], { type: 'text/json' });
    const e = document.createEvent('MouseEvents');
    const a = document.createElement('a');

    a.download = filename;
    a.href = window.URL.createObjectURL(blob);
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':');
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    a.dispatchEvent(e);
  };
}(console));
