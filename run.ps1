$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

try {
    $health = Invoke-RestMethod -Uri "http://127.0.0.1:8000/health" -TimeoutSec 2

    if ($health.status -eq "healthy") {
        Write-Host "Knowledge Brain is already running!"
        Write-Host "Search page: http://127.0.0.1:8000"
        Write-Host "API documentation: http://127.0.0.1:8000/docs"
        exit 0
    }
} catch {
    Write-Host "Starting Knowledge Brain..."
}

python -m uvicorn app.main:app --app-dir task1 --host 127.0.0.1 --port 8000
