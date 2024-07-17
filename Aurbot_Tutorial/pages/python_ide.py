import reflex as rx
from ..ui.base import base_page

def python_ide_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.text_area(id="yourcode", default_value="print('Hello, World!')", width="100%", height="200px"),
            rx.button("Run", on_click=rx.call_script("runit()")),
            rx.html("<div id='output' style='border:1px solid black;height:200px;width:100%;overflow:auto;'></div>"),
            rx.html("<script src='https://cdn.jsdelivr.net/npm/skulpt@0.10.0/dist/skulpt.min.js'></script>"),
            rx.html("<script src='https://cdn.jsdelivr.net/npm/skulpt@0.10.0/dist/skulpt-stdlib.js'></script>"),
            rx.html("""
                <script>
                    function builtinRead(x) {
                        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined) {
                            throw "File not found: '" + x + "'";
                        }
                        return Sk.builtinFiles["files"][x];
                    }

                    function outf(text) {
                        var mypre = document.getElementById("output");
                        mypre.innerHTML = mypre.innerHTML + text;
                    }

                    function runit() {
                        var prog = document.getElementById("yourcode").value;
                        var mypre = document.getElementById("output");
                        mypre.innerHTML = '';
                        Sk.pre = "output";
                        Sk.configure({ output: outf, read: builtinRead });
                        (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
                        var myPromise = Sk.misceval.asyncToPromise(function() {
                            return Sk.importMainWithBody("<stdin>", false, prog, true);
                        });
                        myPromise.then(function(mod) {
                            console.log('success');
                        },
                        function(err) {
                            console.log(err.toString());
                        });
                    }
                    window.runit = runit;
                </script>
            """)
        )
    )

