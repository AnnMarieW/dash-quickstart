
window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        copyToClipboard: function (n, text) {
          if (!navigator.clipboard) {
            alert("copy not available, use ctrl-c");
            return;
          }
          if (n > 0) {
            // removes code block markdown syntax ```
            const trimmed_text = text.replace(/(^```)|(```$)/g, '');
            navigator.clipboard.writeText(trimmed_text).then(function() {
                alert("Copied.  crl-V to paste")
              }, function() {
                alert('copy error')
              });
          }
        }
    }
});


