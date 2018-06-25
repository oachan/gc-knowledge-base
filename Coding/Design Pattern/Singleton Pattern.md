# Singleton Pattern

## 定義

確保一個類別在系統運行的時候，只有一個實體(instance)產生，同時，這個類別必須要提供一個公開的方法讓其他人取得自己的實體。

## Pattern 使用注意
單例模式在多執行緒的應用場合下必須小心使用。
如果當唯一實例尚未創建時，有兩個執行緒同時調用創建方法，那麼它們同時沒有檢測到唯一實例的存在，
從而同時各自創建了一個實例，這樣就有兩個實例被構造出來，從而違反了單例模式中實例唯一的原則。
解決這個問題的辦法是為指示類是否已經實例化的變量提供一個互斥鎖(雖然這樣會降低效率)。


## Python 實作 - 參考資料
[单例模式 | Python One to Million](https://py.windrunner.me/design-patterns/singleton.html)
[Creating a singleton in Python - Stack Overflow](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python)

## Java 實作 - 參考資料
[[設計模式] Singleton Pattern (單例模式) Part1](https://kevingo75.blogspot.tw/2010/12/singleton-pattern-part1.html)
[[設計模式] Singleton Pattern (單例模式) Part2 (解決多執行緒問題) - Update Volatile關鍵字](https://kevingo75.blogspot.tw/2011/01/singleton-pattern-part2.html)
