function joinedLogger(level, sep) {
  //ws.write(`${level}-${sep}\n`);
  function f() {
      var res = "";
      for(var i = 0; i < arguments.length; ++i) {
        let v = arguments[i];
        //ws.write(`${v.level}: ${v.text}\n`);
        if(v.level >= level && v.text.length != 0) {
            res += v.text;
            res += sep;
        }
      }
      res = res.slice(0, res.length-sep.length);
      logger({text: res});
  }
  return f;
}
