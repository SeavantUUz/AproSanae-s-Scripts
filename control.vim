function! AsciiPlayer()
    set nowrap
    set scrolloff=0
    set columns=80        
    set lines=26           
    normal gg
    let i = 1
    while i < 6562
        execute "normal 23\<CR>zt"
        redraw
        let i = i + 1
        sleep 33m
    endwhile
endfunction
command! AsciiPlayer call AsciiPlayer()
