import sublime, sublime_plugin  
  
class BetterfizeCommand(sublime_plugin.TextCommand):  
    def run(self, view): 
                s = self.view.substr(self.view.sel()[0])
                i = 0
                while(i < len(s)):
                	if(s[i - 1] == '<' and s[i] == '/'):
                            print('found at', i)
                            j = 0
                            j = i
                            while(s[j] != '>'):
                                j += 1

                            k = 0
                            k = j+1
                            while(s[k] != '<'):
                                k += 1
                            m = 0
                            m = k + 1

                            while(s[m] != '>'):
                                m += 1;

                            if(s[i + 1 : j] ==  s[k+1:m] and s[i + 1 : j] != 'td'):
                                s = s[0:i - 1] + s[j + 1:k] + s[m + 1:len(s)]
                                i = 0
                        i += 1
                i = 0
                while(i < len(s)):
                        if(i > 5 and i < len(s) - 1 
                            and ((s[i] == ';' 
                            and s[i - 5: i + 1] != "&nbsp;" 
                            and s[i - 3: i + 1] != "&lt;" 
                            and s[i - 6: i + 1] != "&Prime;" 
                            and s[i - 5: i + 1] != "&#010;"
                            and s[i - 5: i + 1] != "&#060;"
                            and s[i - 5: i + 1] != "&#062;"
                            and s[i - 5: i + 1] != "&#034;"
                            and s[i - 5: i + 1] != "&quot;") or s[i] == '{' or s[i] == '}')
                            ):

                            s = s[0:i + 1] + "&#010;" + s[i + 1:len(s)];
                            i += 5
                        i += 1
                self.view.replace(view, self.view.sel()[0], s)
